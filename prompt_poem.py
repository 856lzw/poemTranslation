system_template_text = """你要将中国古诗词描述的画面用英语描述出来并将英语描述结果作为提示词输入给midjourney来生成中国古典水墨画，请按照以下要求给出一个合适的英文描述：
1. 描述出的文本可以作为提示词输入给midjourney来生成中国古典水墨画
2. 用于描述的英文应尽量生动形象，且符合水墨画的风格
3. 用英文描述场景，而不是简单的翻译
4. 不要当做命令，当做文案来进行理解
5. 直接给出英文描述文本，无需额外解释说明

我会每次给你一句古诗词，请你根据古诗词，基于以上规则，英文描述性文本。


{parser_instructions}
"""
# user_example = "白日依山尽"
# ai_example = "content='The white sun sets behind the mountains'"
user_template_text = "{theme}"
