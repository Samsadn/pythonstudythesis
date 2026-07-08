# Part 4 — Reflection on ChatGPT Use

## 1. Did you ask ChatGPT for hints, explanations, debugging help, verification, or a full solution?

I used ChatGPT mostly for explanations and verification. I asked it to explain why `input()` gives text and why I need to use `float()`. I also asked for help understanding where the division-by-zero check should be placed. I did not start by asking for a full solution. I tried to understand the task first and then used ChatGPT when I was unsure.

## 2. Which ChatGPT answer helped you understand the task best?

The most helpful answer was the explanation about strings and numbers. The example that `"10" + "5"` becomes `"105"` helped me understand why the broken calculator code does not work correctly. After that, using `float()` made more sense to me.

## 3. Did you copy any code directly? If yes, did you understand it afterwards?

I copied the basic idea of checking `if right_number == 0` before division, but I wrote it using my own variable names and placed it inside my own calculator structure. I understood afterwards that the check is needed before the division happens, because Python cannot divide by zero.

## 4. Could you explain the calculator without ChatGPT now?

Yes, I could explain the basic calculator now. It asks for two numbers, converts them using `float()`, asks for an operation, and then uses `if`, `elif`, and `else` to decide which calculation to perform. I can also explain how invalid operations and division by zero are handled.

## 5. What would you try alone before asking ChatGPT next time?

Next time I would first write the input part and one operation myself. Then I would test it before adding the other operations. If something goes wrong, I would read the error message and try to fix it once or twice before asking ChatGPT.

## 6. At what point did you decide to ask ChatGPT instead of continuing independently?

I decided to ask ChatGPT when I understood the basic structure but was unsure why input values behaved like text. I also asked when I wanted to confirm the safest way to handle division by zero.
