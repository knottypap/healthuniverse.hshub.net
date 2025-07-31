def generate_study_plan(time, passage):
    if time <= 5:
        return {
            "mode": "Quick Reflection",
            "steps": [
                "Read passage: " + passage,
                "Pray: Thank God, ask for wisdom",
                "Reflect: 1 takeaway"
            ]
        }
    elif time <= 15:
        return {
            "mode": "Daily Devotion",
            "steps": [
                "Read passage + 2 cross-references",
                "Pray over message",
                "Journal 1 reflection + 1 prayer"
            ]
        }
    else:
        return {
            "mode": "Deep Dive",
            "steps": [
                "Read full chapter around " + passage,
                "Compare 3 translations (e.g., ESV, NLT, KJV)",
                "Word study (key Greek/Hebrew term)",
                "Write personal application",
                "Close in structured prayer"
            ]
        }

def generate_prayer(mood, passage):
    base = "Heavenly Father, "
    if mood == "anxious":
        base += "thank You for being my peace. Help me trust in Your promises as shown in " + passage + ". "
    elif mood == "grateful":
        base += "I praise You for Your goodness and faithfulness. "
    base += "Let Your Word shape my heart today. In Jesus' name, Amen."
    return base
