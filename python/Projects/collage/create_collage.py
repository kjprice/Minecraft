from math import floor
import os

import cv2
import numpy as np

from ...MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from ...common.images import ResizeImage

class CollageFunction(MinecraftFunction):
    z_offset = 0
    def __init__(self, behavior_pack, namespace, z_offset=0):
        self.z_offset = z_offset
        super().__init__(namespace, behavior_pack)
    def build(self):
        pass
    def create_function(self, row, column, name, depth=0):
        depth = depth - self.z_offset
        self.run('setblock ~{} ~{} ~{} {}:{}'.format(column, row, depth, self.function_name, name))

# The resolution for each image block
MAX_BLOCK_DIM = 16

class Collage():
    img = None
    img_path = None
    behavior_pack = None
    resource_pack = None
    namespace = None
    canvas_dimensions = None
    resize_ratio = None
    def __init__(self, behavior_pack, resource_pack, namespace, img_filename: str, resize_ratio: float = None, resize_block_height: int = None, resize_max_height: int = None, starting_x: int = 0, z_offset = 10) -> None:
        self.behavior_pack = behavior_pack
        self.resource_pack = resource_pack
        self.namespace = namespace
        self.img_path = os.path.join('data', img_filename)

        self.resize_ratio = resize_ratio
        self.resize_max_height = resize_max_height
        if resize_block_height is not None:
            self.resize_max_height = resize_block_height * MAX_BLOCK_DIM
        self.starting_x = starting_x

        img = self.load_image()
        self.img = self.crop_image(img)
        self.img = self.resize_image(img)
        self.function = CollageFunction(self.behavior_pack, namespace, z_offset=z_offset)

        self.create_blocks()
    
    def resize_image(self, img):
        old_dimensions = img.shape[:2]
        print('Old Dimensions: {} X {}'.format(old_dimensions[0], old_dimensions[1]))

        resized_image = img
        if self.resize_ratio is not None:
            resized_image = ResizeImage(img).by_ratio(self.resize_ratio)
        if self.resize_max_height is not None:
            resized_image = ResizeImage(img).by_max_height(self.resize_max_height)

        new_dimensions = resized_image.shape[:2]
        print('New Dimensions: {} X {}'.format(new_dimensions[0], new_dimensions[1]))

        return resized_image

    def crop_image(self, img):
        img_height, img_width, channels = img.shape
        max_height = floor(img_height / MAX_BLOCK_DIM) * MAX_BLOCK_DIM
        max_width = floor(img_width / MAX_BLOCK_DIM) * MAX_BLOCK_DIM

        return img[0:max_height, 0:max_width, :]
    def load_image(self):
        script_filepath = os.path.dirname(os.path.realpath(__file__))
        return cv2.imread(os.path.join(script_filepath, self.img_path))

    def save_image(self, img_name, img):
        script_filepath = os.path.dirname(os.path.realpath(__file__))
        cv2.imwrite(os.path.join(script_filepath, img_name), img)

    def create_blocks(self):
        img = self.img
        blocks_y_count = int(img.shape[0] / MAX_BLOCK_DIM)
        blocks_x_count = int(img.shape[1] / MAX_BLOCK_DIM)

        self.canvas_dimensions = (blocks_y_count, blocks_x_count)
    
        print('Creating {}x{} = {} blocks'.format(
            blocks_y_count,
            blocks_x_count,
            blocks_x_count * blocks_y_count
        ))

        blocks_images = []
        for y in range(blocks_y_count):
            for x in range(blocks_x_count):
                x1 = x * MAX_BLOCK_DIM
                x2 = x1 + MAX_BLOCK_DIM
                y1 = y * MAX_BLOCK_DIM
                y2 = y1 + MAX_BLOCK_DIM

                img_array = img[y1:y2, x1:x2, :]
                blocks_images.append(
                    {
                        'img_array': img_array,
                        'row': y,
                        'column': x
                    }
                )
        self.save_block_images(blocks_images)
    def save_block_images(self, blocks_images):
        for i, img_data in enumerate(blocks_images):
            img_array = img_data['img_array']
            row = img_data['row']
            column = img_data['column']
            self.save_block_image(img_array, row, column)

        self.function.run_all()
    def save_block_image(self, img_array, row, column):
        y_offset, x_offset = self.canvas_dimensions
        name="{}_collage{}x{}".format(self.namespace, str(row), str(column))
        self.behavior_pack.save_block(self.namespace, name)
        self.resource_pack.save_block(img_array, self.namespace, name)

        x = column + self.starting_x

        # uses offset so that image is built from top-down
        row_with_offset = y_offset - row
        self.function.create_function(row_with_offset, x, name)

        # creates backside of image - flip original image
        x_with_offset = self.starting_x + x_offset - column - 1
        self.function.create_function(row_with_offset, x_with_offset, name, depth=-1)
        


