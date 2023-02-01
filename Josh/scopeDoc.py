# showing difference of scope
# demonstrating global vs local scope

first_name = input('Please type your first name: ')
last_name = input('Please type your last name: ')


# above are global scoped variables
# These variables are set on a 'global' scale and accessable anywhere (inside and outside of functions)
# below we will create a function with 'local' scope


# below is a value-return function
def make_full_name_value_return (fName, LName):
    fullname = fName + ' ' + LName
    nickname = fName + 'sky'
    dogName = LName + 'good-boy'
    return fullname




full_name = make_full_name_value_return(first_name, last_name)


print(full_name)
