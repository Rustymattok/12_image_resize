import argparse
import os
from PIL import Image


def get_image(path_to_original):
    if not os.path.exists(path_to_original):
        print('not correct path to file')
        return None
    return Image.open(path_to_original)


def get_size(size_image, width_resize, height_resize, scale_resize):
    image_width, image_height = size_image
    if width_resize is not None and height_resize is None:
        size_image = (
            int(width_resize),
            int(round(float(width_resize) * float(image_height / image_width)))
        )
    if height_resize is not None and width_resize is None:
        size_image = (
            int(round(float(height_resize)*float(image_width/image_height))),
            int(height_resize)
        )
    if scale_resize is not None:
        size_image = (
            int(image_width) * int(scale_resize),
            int(image_height) * int(scale_resize)
        )
    return size_image


def save_image(image, path_to_result):
    if path_to_result.find(".jpg") > 0 or path_to_result.find(".png") > 0:
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
    parser = create_parser()
    args = parser.parse_args()
    file_path = args.filepath
    file_outpath = args.output
    width = args.width
    height = args.height
    scale = args.scale
    image_input = get_image(file_path)
    if image_input is not None:
        image_size = image_input.size
        resize_parameter = get_size(image_size, width, height, scale)
        print(resize_parameter)
        resize_image = image_input.resize(resize_parameter)
        if file_outpath is None:
            file_outpath = get_file_name_out(resize_image)
        save_image(resize_image, file_outpath)


if __name__ == '__main__':
    main()
