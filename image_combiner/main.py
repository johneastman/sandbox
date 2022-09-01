from PIL import Image


def combine_images(
        image_paths: list[str],
        new_image_path: str,
        is_vertical: bool = True) -> None:
    """Combine a list of images into one image

    :param image_paths: list of paths to images that will be combined into one image
    :type image_paths: str
    :param new_image_path: path to save new image
    :type new_image_path: str
    :param is_vertical: how the images should be combined (vertically or horizontally). Defaults to vertically (True).
    :type is_vertical: bool
    :return: None
    """
    images = [Image.open(image_path) for image_path in image_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths) if is_vertical else sum(widths)
    max_height = sum(heights) if is_vertical else max(heights)

    new_image = Image.new("RGB", (total_width, max_height))

    y_offset = 0
    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, y_offset))

        if is_vertical:
          y_offset += image.size[1]
        else:
          x_offset += image.size[0]

    new_image.save(new_image_path)


if __name__ == "__main__":
    image_paths = [
        "image_1.jpg",
        "image_2.jpg",
    ]
    combine_images(image_paths, "image.jpg")
