def extract_triplet(message):

    words = message.split()

    if "uses" in words:

        try:
            source = words[0]
            relation = "uses"
            target = words[-1]

            return {
                "source": source,
                "relation": relation,
                "target": target
            }

        except:
            return None

    return None