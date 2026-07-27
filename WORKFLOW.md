# AI Workflow Comparison

## Feature
I built a Settings Form with validation using two different AI prompting workflows.

## Round 1 – Vague Prompt
I used a simple prompt: "Create a settings form for my React app."

The AI generated a basic form with minimal validation and limited accessibility. I had to manually review the code, fix validation issues, and improve the UI before it was usable.

## Round 2 – Precise Prompt
I started a fresh AI session and used a detailed prompt with clear requirements, including React Hook Form, Zod validation, accessibility, responsive design, and tests. I also asked the AI to review its own code and generate tests.

The resulting code was cleaner, better organized, and required fewer manual changes. The generated tests helped verify the implementation.

## Comparison
The vague prompt produced working code quickly but required more debugging and review. The precise prompt took longer to write but saved time overall because the generated code followed project requirements, included validation, and handled edge cases better. Accessibility and maintainability were also improved.

## AI Mistake I Found
During the second round, I noticed the AI forgot to disable the submit button while the form was submitting. I corrected this before committing the changes.

## Lessons Learned
This exercise showed that writing clear prompts with constraints and verification steps produces higher-quality code and reduces overall development time. Going forward, I will use structured prompts and include testing and review instructions in my AI workflow.