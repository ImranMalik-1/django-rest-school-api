class Util:

    def check_if_int(value):
        is_integer = True
        try:
            int(value)
        except ValueError:
            is_integer = False
        return is_integer
