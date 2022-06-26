# import re
#
# from config.public_opinion_key_words import COMMON_PUBLIC_OPINION_KEY_WORDS
#
#
# def common_key_words_match(comment):
#     common_public_opinion_key_words = COMMON_PUBLIC_OPINION_KEY_WORDS
#     for m in range(0, len(common_public_opinion_key_words)):
#         if re.findall(common_public_opinion_key_words[m], comment):
#             print("用户评论命中通用关键字")