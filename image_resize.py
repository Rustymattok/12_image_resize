import argparse
import os
from PIL import Image


def get_image(path_to_original):
    if not os.path.exists(path_to_original):
        return None
    return Image.open(path_to_original)


def get_resized_image(image, width_resized, height_resized, scale_resized):
    if image is None:
        return None
    image_width, image_height = image.size
    resized_image = None
    if width_resized is not None \
            and int(width_resized) > 0 \
            and height_resized is None:
        resized_image = (
            int(width_resized),
            int(round(
                float(width_resized) * float(image_height / image_width)
            ))
        )
    if height_resized is not None \
            and int(height_resized) > 0 \
            and width_resized is None:
        resized_image = (
            int(round(
                float(height_resized) * float(image_width / image_height)
            )),
            int(height_resized)
        )
    if scale_resized is not None \
            and int(scale_resized) > 0 \
            and width_resized is None \
            and height_resized is None:
        resized_image = (
            int(image_width) * int(scale_resized),
            int(image_height) * int(scale_resized)
        )
    if resized_image is None:
        return None
    return image.resize(resized_image)


def save_image(image, path_to_result):
    if not os.path.exists(path_to_result):
        image.save(path_to_result)
    else:
        return None


def get_file_name_output(image):
    width_image, height_image = image.size
    path_file_out = 'pic_{width}x{height}.jpg'.\
        format(width=str(width_image), height=str(height_image))
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
    image = get_image(file_path)
    if file_outpath is not None and not os.path.exists(file_outpath):
        print("not correct directory")
        return
    if image is None:
        print('not correct file path')
        return
    image_resized = get_resized_image(image, width, height, scale)
    if image_resized is None:
        print('not correct command')
        return
    if file_outpath is None:
        file_outpath = get_file_name_output(image_resized)
    else:
        file_outpath = file_outpath + get_file_name_output(image_resized)
    if save_image(image_resized, file_outpath) is None:
        print('you try to rewrite current file')


if __name__ == '__main__':
    main()
