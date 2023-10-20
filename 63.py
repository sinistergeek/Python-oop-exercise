class CustomDic(dict):

    def is_any_str_value(self):
        flag = False
        for key in self:
            if isinstance(self[key],str):
                flag= True
                break
        return flag
