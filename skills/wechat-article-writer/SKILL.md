---
name: wechat-article-writer
description: Write a review-ready WeChat Official Account article from a verified fact list. Use when the user wants a 公众号 article drafted from given facts/topics, in a clear explanatory style, without inventing facts, and formatted with fixed WeChat sections for human review before publishing.
---

# WeChat Article Writer

## Inputs
- A title (or 3 candidate titles to choose from)
- A fact list: only facts the user provided or that carry a named source
- Sources with names/URLs where available

## Hard rules
1. Use ONLY the given facts. Never invent numbers, names, dates, quotes or reactions.
2. Allegations, claims and disputed statements must be attributed ("据报道", "据 X 称"), never stated as fact.
3. Do not predict outcomes (elections, wars, prices). Describe what is known and what is still unknown.
4. One topic per article. If the fact list is too thin for 800+ words, say so and list what is missing instead of padding.

## Workflow
1. Check the fact list: mark anything unsourced; ask or flag before writing.
2. Outline: 导语 (what happened, one or two sentences) → 发生了什么 → 为什么重要 → 还不清楚 → 结尾讨论.
3. Draft 1000–1500 Chinese characters per 1000-word target the user sets; short paragraphs, one idea each.
4. Bold only key numbers and conclusions. Subheadings exactly as the outline.
5. End with a sources block (small print): source name + link, domestic primary sources first when the user works in Chinese media.

## Output
Markdown with `##` section headings, title as `#`. Add a one-line note at the top listing any facts that still need verification. The draft is review-only: never claim it was published or pushed anywhere.

## Self-check before delivering
- [ ] Every number/name/date appears in the input fact list
- [ ] Every disputed claim is attributed
- [ ] No outcome predictions
- [ ] Sources block present
