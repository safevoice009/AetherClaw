\"\"\"
🌌 AetherTranslator: Global Reach Accelerator (v1.0)
Translates the README into major global languages for international SEO.
\"\"\"

import os
from utils.llm_session import ask_llm

LANGUAGES = {
    \"CN\": \"Mandarin Support (PRC/China)\",
    \"ES\": \"Spanish Support (LATAM/Spain)\",
    \"HI\": \"Hindi Support (India)\",
    \"JP\": \"Japanese Support (Japan)\"
}

def translate_readme():
    if not os.path.exists(\"README.md\"):
        print(\"❌ README.md not found.\")
        return
        
    with open(\"README.md\", \"r\", encoding=\"utf-8\") as f:
        original_content = f.read()

    print(\"🌌 Initiating Global Reach Expansion...\")
    
    for code, desc in LANGUAGES.items():
        print(f\"   Translating for {desc}...\")
        prompt = f\"\"\"
Translate the following README.md content into {desc}. 
Maintain all technical formatting, Markdown structure, and code blocks exactly as they are. 
Translate only the prose/text descriptions.

CONTENT:
{original_content}
\"\"\"
        try:
            translation = ask_llm(prompt)
            output_file = f\"README_{code}.md\"
            with open(output_file, \"w\", encoding=\"utf-8\") as f:
                f.write(translation)
            print(f\"✅ Generated: {output_file}\")
        except Exception as e:
            print(f\"❌ Translation failed for {code}: {e}\")

if __name__ == \"__main__\":
    translate_readme()
