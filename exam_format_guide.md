# Exam Format Guide

To automatically generate a practice exam dashboard, your Markdown (`.md`) file needs to follow this simple structure.

## Document Structure

1. **Exam Title**: The very first Heading 1 (`#`) in the file will become the exam title.
2. **Domains**: Use Heading 2 (`##`) to define domains/categories. All questions that follow will belong to that domain until the next `##` header.
3. **Questions**: Start a question with its number followed by a period and the word "Question" or simply start with a bold `**Question 1:**` or `**Question:**`.
4. **Options**: Provide options using a standard list format (`- A)` , `- B)`, etc.).
5. **Answer**: Provide the correct answer directly below the options using `**Answer:**` or `Answer:`. You can provide just the letter (e.g., `B`) or the full text.
6. **Explanation**: Provide an explanation using `**Explanation:**` or `Explanation:`.

## Example

```markdown
# AZ-900 Microsoft Azure Fundamentals

## Domain 1: Cloud Concepts

**Question 1:** What is the primary benefit of cloud computing over on-premises infrastructure?
- A) You own all the hardware.
- B) You pay only for what you use (CapEx to OpEx).
- C) You have complete physical control over the data center.
- D) It does not require an internet connection.
**Answer:** B
**Explanation:** Cloud computing introduces a Consumption-based model where you move from fixed Capital Expenditure (CapEx) to variable Operational Expenditure (OpEx).

**Question 2:** Which cloud model allows you to run applications without managing underlying servers?
- A) IaaS (Infrastructure as a Service)
- B) PaaS (Platform as a Service)
- C) SaaS (Software as a Service)
- D) Serverless Computing
**Answer:** D
**Explanation:** Serverless computing abstracts server management completely, automatically scaling to meet demand.

## Domain 2: Core Azure Services

**Question 3:** ...
```
