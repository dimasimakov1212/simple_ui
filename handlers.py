def get_birds_list(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "birds_list_btn":
        hashMap.put("toast", 'Список птиц')

        return hashMap
