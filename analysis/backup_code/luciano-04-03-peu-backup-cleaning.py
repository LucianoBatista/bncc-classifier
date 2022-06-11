# #%%
# # Transforming all of questions to string
# df_bncc_copy_targets_bncc["questions"] = df_bncc_copy_bncc["questions"].astype(
#     str
# )
# #%%
# # Removing html tags from questions
#
# df_bncc_copy_targets_bncc["questions_tags_free"] = df_bncc_copy_targets_bncc[
#     "questions"
# ].apply(html.unescape)
#
# df_bncc_copy_targets_bncc.head()
# #%%
# # Removing HTML
# df_bncc_copy_targets_bncc["questions_html_free"] = df_bncc_copy_targets_bncc[
#     "questions_tags_free"
# ].apply(lambda text: cleaning.remove_html(text))
# df_bncc_copy_targets_bncc.head()
# #%%
# # Lower Casing
# df_bncc_copy_targets_bncc["questions_lower"] = df_bncc_copy_targets_bncc[
#     "questions_html_free"
# ].str.lower()
#
# df_bncc_copy_targets_bncc.head()
# #%%
# # Removing punctuation of the questions
# df_bncc_copy_targets_bncc["questions_punctuation_free"] = df_bncc_copy_targets_bncc[
#     "questions_lower"
# ].apply(lambda text: cleaning.remove_punctuation(text))
# df_bncc_copy_targets_bncc.head()
# #%%
# df_bncc_copy_targets_bncc["questions_no_italic_quotes"] = df_bncc_copy_targets_bncc[
#     "questions_punctuation_free"
# ].apply(cleaning.remove_italic_quotes)
# df_bncc_copy_targets_bncc["questions_no_open_quotes"] = df_bncc_copy_targets_bncc[
#     "questions_no_italic_quotes"
# ].apply(cleaning.remove_open_quotes)
# df_bncc_copy_targets_bncc["questions_no_end_quotes"] = df_bncc_copy_targets_bncc[
#     "questions_no_open_quotes"
# ].apply(cleaning.remove_end_quotes)
#
# df_bncc_copy_targets_bncc["questions_no_italic_dquotes"] = df_bncc_copy_targets_bncc[
#     "questions_no_end_quotes"
# ].apply(cleaning.remove_italic_dquotes)
# df_bncc_copy_targets_bncc["questions_no_open_dquotes"] = df_bncc_copy_targets_bncc[
#     "questions_no_italic_dquotes"
# ].apply(cleaning.remove_open_dquotes)
# df_bncc_copy_targets_bncc["questions_no_end_dquotes"] = df_bncc_copy_targets_bncc[
#     "questions_no_open_dquotes"
# ].apply(cleaning.remove_end_dquotes)
#
# df_bncc_copy_targets_bncc["questions_no_quotes"] = df_bncc_copy_targets_bncc[
#     "questions_no_end_dquotes"
# ].apply(cleaning.remove_quote)
