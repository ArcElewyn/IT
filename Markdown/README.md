# Guide to Markdown Syntax

## Introduction

This guide presents the main Markdown syntax as recommended by [Markdown Guide](https://www.markdownguide.org/cheat-sheet/). You can copy and modify this document to learn or review Markdown syntax.

---

## Headings

Use the `#` character followed by a space to create headings. The more `#` characters, the smaller the heading:

```markdown
# Level 1 Heading
## Level 2 Heading
### Level 3 Heading
```

# Level 1 Heading  
## Level 2 Heading  
### Level 3 Heading  

---

## Bold and Italic Text

To display text in **bold**, surround it with two asterisks (`**`) or two underscores (`__`):

```markdown
**Bold text**
__Bold text__
```
**Bold text**  
__Bold text__

To display text in *italic*, use an asterisk (`*`) or an underscore (`_`):

```markdown
*Italic text*
_Italic text_
```
*Italic text*  
_Italic text_  

---

## Block Quotes

Use `>` to create a block quote:

```markdown
> This is a block quote.
```
> This is a block quote.

To nest quotes, add additional `>` characters:

```markdown
> Main quote
>> Nested quote
```
> Main quote  
>> Nested quote  

_Note: To exit a quote block, leave an empty line._

---

## Lists

### Unordered Lists

Use `-`, `*`, or `+` followed by a space:

```markdown
- Item 1
- Item 2
```
- Item 1  
- Item 2  

```markdown
* Item 1
* Item 2
```
* Item 1  
* Item 2  

```markdown
+ Item 1
+ Item 2
```
+ Item 1  
+ Item 2  

### Ordered Lists

Use numbers followed by a period (`1.`):

```markdown
1. Item 1
2. Item 2
```
1. Item 1  
2. Item 2  

---

## Code and Formatting

To display inline code, enclose text with backticks (\`):

```markdown
Here is an `inline code example`.
```
Here is an `inline code example`.

To display a block of code, use three backticks (\`\`\`) before and after the block:

```markdown
```
\`\`\`
print("Hello, world!")
\`\`\`
```
print("Hello, world!")
```

---

## Horizontal Rules and Line Breaks

To insert a horizontal line, use `---`:

```markdown
---
```
---

To force a line break, add a backslash (`\`) at the end of the line or leave an empty line:

```markdown
First line.\
Second line.
```
First line.\
Second line.

```markdown
First line.

Second line.
```
First line.  

Second line.  

---

## Links and Images

### Links

Use `[text](URL)` to add a link:

```markdown
[Google](https://www.google.com)
```
[Google](https://www.google.com)

### Images

Use `![alt text](URL)` to add an image:

```markdown
![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
```
![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

---

## Spaces and Indentation

Use `&nbsp;` to insert non-breaking spaces:

```markdown
Text with&nbsp;&nbsp;&nbsp;&nbsp;four spaces.
```
Text with&nbsp;&nbsp;&nbsp;&nbsp;four spaces.

Use `&emsp;` for an em space (tab):

```markdown
Text with&emsp;a tab.
```
Text with&emsp;a tab.

---

This guide covers the essential basics of Markdown syntax. For more details, please refer to [Markdown Guide](https://www.markdownguide.org/).
