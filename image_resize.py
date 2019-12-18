import argparse
import os
import sys
from PIL import Image


def get_image(path_to_original):
    if not os.path.exists(path_to_original):
        print('not correct path to file')
        return None
    return Image.open(path_to_original)


def get_resize_image_by_width(path_to_original, width):
    image = get_image(path_to_original)
    if image is None:
        return
    image_width, image_height = image.size
    resized_image = image.resize(
        (width, int(width*image_height/image_width))
    )
    return resized_image


def get_resize_image_by_height(path_to_original, height):
    image = get_image(path_to_original)
    if image is None:
        return
    image_width, image_height = image.size
    resized_image = image.resize(
        (int(round(float(height)*image_width/image_height)), int(height))
    )
    return resized_image


def get_resize_image_by_size(path_to_original, width, height):
    image = get_image(path_to_original)
    if image is None:
        return
    image_width, image_height = image.size
    if int(image_height/image_width) != (height/width):
        print('not proportional')
    resized_image = image.resize((width, height))
    return resized_image


def get_resize_image_by_scale(path_to_original, scale):
    image = get_image(path_to_original)
    if image is None:
        return
    image_width, image_height = image.size
    resized_image = image.resize(
        (image_width * scale, image_height * scale)
    )
    return resized_image


def save_image(image, path_to_result):
    if path_to_result.find(".jpg") > 0 or path_to_result.find(".png") > 0:
        print("test")
        image.save(path_to_result)
    else:
        print('not correct out_path')


def get_file_name_out(image):
    width_image, height_image = image.size
    file_out = 'pic__' + str(width_image) + 'x' + str(height_image) + '.jpg'
    return file_out


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--filepath',
        required=True,
        help='command - file path for re-size'
    )
    parser.add_argument(
        '-o',
        '--output',
        required=False,
        help='command - file path for save result'
    )
    parser.add_argument(
        '-w',
        '--width',
        required=False,
        help='command width'
    )
    parser.add_argument(
        '-ht',
        '--height',
        required=False,
        help='command height'
    )
    parser.add_argument(
        '-s',
        '--scale',
        required=False,
        help='command scale'
    )
    return parser


def main():
    resize_image = None
    parser = create_parser()
    args = parser.parse_args()
    file_path = args.filepath
    file_outpath = args.output
    width = args.width
    height = args.height
    scale = args.scale
    if width is None and height is None and scale is not None:
        resize_image = get_resize_image_by_scale(file_path, int(scale))
    if width is not None and height is None and scale is None:
        resize_image = get_resize_image_by_width(file_path, int(width))
    if height is not None and width is None and scale is None:
        resize_image = get_resize_image_by_height(file_path, height)
    if width is not None and height is not None and scale is None:
        resize_image = get_resize_image_by_size(
            file_path, int(width), int(height)
        )
    if width is None and height is None and scale is not None:
        resize_image = get_resize_image_by_scale(file_path, scale)
    if file_outpath is None:
        file_outpath = get_file_name_out(resize_image)
    save_image(resize_image, file_outpath)


if __name__ == '__main__':
    main()
