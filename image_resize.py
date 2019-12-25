import argparse
import os
from PIL import Image


def get_image(path_to_original):
    if not os.path.exists(path_to_original):
        return None
    return Image.open(path_to_original)


def validate(width, height, scale):
    if scale and (width or height):
        return False
    if (height and height < 0) or (width and width < 0):
        return False
    if width and height:
        return False
    return True


def get_resized_image(image, width, height, scale):
    if image is None:
        return None
    image_width, image_height = image.size
    image_new_size = None
    if width:
        image_new_size = (width, round(width * image_height / image_width))
    if height:
        image_new_size = (round(height * image_width / image_height), height)
    if scale:
        image_new_size = (int(image_width * scale), int(image_height * scale))
    return image.resize(image_new_size)


def save_image(image, path_to_result):
    image.save(path_to_result)


def get_file_name_output(path_to_original, image, file_outpath):
    width_image, height_image = image.size
    format_file = path_to_original[-3:]
    path_file_out = 'pic_{width}x{height}.{format}'. \
        format(width=width_image, height=height_image, format=format_file)
    if file_outpath is not None:
        path_file_out = os.path.join(file_outpath, path_file_out)
    return path_file_out


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
        type=str,
        required=False,
        help='command - file path  to directory for save result'
    )
    parser.add_argument(
        '-w',
        '--width',
        type=int,
        required=False,
        help='command width'
    )
    parser.add_argument(
        '-ht',
        '--height',
        type=int,
        required=False,
        help='command height'
    )
    parser.add_argument(
        '-s',
        '--scale',
        type=float,
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
    image = get_image(file_path)
    if not validate(width, height, scale):
        print('not correct command')
        return
    if file_outpath is not None and not os.path.isdir(file_outpath):
        print("not correct directory")
        return
    if image is None:
        print('not correct file path')
        return
    image_new = get_resized_image(image, width, height, scale)
    file_outpath = get_file_name_output(file_path, image_new, file_outpath)
    if os.path.isfile(file_outpath):
        print('you try to rewrite current file')
    save_image(image_new, file_outpath)


if __name__ == '__main__':
    main()
