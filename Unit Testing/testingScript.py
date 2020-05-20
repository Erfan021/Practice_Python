# Testing

def stuff_do(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Enter number please'
    except ValueError as err:
        return err




