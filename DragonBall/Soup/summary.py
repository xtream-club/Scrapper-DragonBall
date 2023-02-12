class Summary:

    @classmethod
    def clean_list_summary(cls, list_sumary, remove):
        summary = [x for x in list_sumary if x != '']
        return cls.__convert_list_summary_to_dict(summary[remove[0]:remove[1]])

    @staticmethod
    def __convert_list_summary_to_dict(summary):
        dictionary = {}
        current_key = None
        for item in summary:
            if "." not in item:
                current_key = item.lstrip('1234567890.').strip()
                dictionary[current_key] = []
            else:
                dictionary[current_key].append(item.lstrip('1234567890.').strip())
        return dictionary