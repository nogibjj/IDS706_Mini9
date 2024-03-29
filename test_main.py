from main import summary_desc, visual, save_to_md

# import pandas as pd


def test_summary_desc():
    result = summary_desc()

    # mean
    assert result.loc["mean", "calories"] == 106.88311688311688

    # median
    assert result.loc["50%", "protein"] == 3.0

    # standard deviation
    assert result.loc["std", "fat"] == 1.006472559480393


def test_visual():
    visual()


def test_save_to_md():
    save_to_md()


if __name__ == "__main__":
    test_summary_desc()
    test_visual()
    test_save_to_md()
