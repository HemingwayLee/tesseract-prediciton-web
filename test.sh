
# Output with confidence level
# tesseract images/en.png output_en_test --oem 1 -l eng tsv
# tesseract images/jp.png output_jp_clean --oem 1 -l jpn tsv

# Output
tesseract images/en.png - -l eng
tesseract images/jp.png - -l jpn

