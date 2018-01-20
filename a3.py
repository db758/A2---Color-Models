""" 
Functions for Assignment A3

This file contains the functions for the assignment.
You should replace the stubs with your own implementations.

a3
Debasmita Bhattacharya (db758) Myka Umali (meu22)
October 1, 2017
"""
import cornell
import math


def complement_rgb(rgb):
    """
    Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG.  FIX IT
    return cornell.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def round(number, places):
    """
    Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3
    """
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is left of 
    #      the decimal place.  For example, if you are rounding 100.556 to the first 
    #      decimal place, the number becomes 1005.56.  If you are rounding to the second 
    #      decimal place, it becomes 10055.6.  If you are rounding 100.556 to the nearest 
    #      integer, it remains 100.556.
    #   2. Add 0.5 to this number
    #   3. Convert the number to an int, cutting it off to the right of the decimal.
    #   4. Shift the number back "to the right" the same amount that you did to the left.
    #      Suppose that in step 1 you converted 100.556 to 1005.56.  In this case, 
    #      divide the number by 10 to put it back.
    
    shifting_left = number*10**places
    add_half = shifting_left + 0.5
    convert_to_int = int(add_half)
    shifting_right = convert_to_int/(10**places)
    
    return shifting_right


def str5(value):
    """
    Returns: value as a string, but expand or round to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Note:Obviously, you want to use the function round() that you just defined. 
    # However, remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    
    value_as_string = str(value)
    
    if '.' in value_as_string:
        
        point = value_as_string.index('.')
        string = round(value, 4-point)
        length = len(str(string))
        if length < 5:
            string = str(string) + (5-length)*'0'
    
    else:
        length = len(value_as_string)
        string = value_as_string + '.' + (4-length)*'0'
    
    return str(string)


def str5_cmyk(cmyk):
    """
    Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces
    after the commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    
    c = str5(cmyk.cyan)
    m = str5(cmyk.magenta)
    y = str5(cmyk.yellow)
    k = str5(cmyk.black)
    
    return '(' + c + ', ' + m + ', ' + y + ', ' + k + ')' 


def str5_hsv(hsv):
    """
    Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    
    h = str5(hsv.hue)
    s = str5(hsv.saturation)
    v = str5(hsv.value)
    
    return '(' + h + ', ' + s + ', ' + v + ')'   


def rgb_to_cmyk(rgb):
    """
    Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    
    r_new = rgb.red/255.0
    g_new = rgb.green/255.0
    b_new = rgb.blue/255.0
    
    c_new = 1 - r_new
    m_new = 1 - g_new
    y_new = 1 - b_new
    
    if c_new == 1 and m_new == 1 and y_new == 1:
        c_final = 0
        m_final = 0
        y_final = 0
        k_final = 1
        
        c_final_final = c_final *100.0
        m_final_final = m_final *100.0
        y_final_final = y_final *100.0
        k_final_final = k_final *100.0
        
        
    else:
        k_final = min(c_new, m_new, y_new)
        c_final = (c_new - k_final)/(1 - k_final)
        m_final = (m_new - k_final)/(1 - k_final)
        y_final = (y_new - k_final)/(1 - k_final)
        
        c_final_final = c_final * 100.0
        m_final_final = m_final * 100.0
        y_final_final = y_final * 100.0
        k_final_final = k_final * 100.0
        
    
    return cornell.CMYK(c_final_final, m_final_final, y_final_final, \
                        k_final_final)


def cmyk_to_rgb(cmyk):
    """
    Returns : color CMYK in space RGB.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the 
    # same way as the RGB numbers in rgb_to_cmyk()
    
    c_new = cmyk.cyan/100.0
    m_new = cmyk.magenta/100.0
    y_new = cmyk.yellow/100.0
    k_new = cmyk.black/100.0
    
    r_final = (1-c_new)*(1 - k_new)
    g_final = (1-m_new)*(1-k_new)
    b_final = (1-y_new)*(1-k_new)
    
    r_finale = int(round((r_final*255),0))
    g_finale = int(round((g_final*255),0))
    b_finale = int(round((b_final*255),0))
    
    return cornell.RGB(r_finale, g_finale, b_finale)


def rgb_to_hsv(rgb):
    """
    Return: color rgb in HSV color space.
    
    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    
    r_new = rgb.red/255.0
    g_new = rgb.green/255.0
    b_new = rgb.blue/255.0
    MAX = max(r_new, g_new, b_new)
    MIN = min(r_new, g_new, b_new)
    
    if MAX == MIN:
        H = 0
    elif MAX == r_new and g_new >= b_new:
        H = 60.0*(g_new - b_new)/(MAX-MIN)
    elif MAX == r_new and g_new < b_new:
        H = 60.0*(g_new - b_new)/(MAX-MIN) + 360.0
    elif MAX == g_new:
        H = 60.0*(b_new - r_new)/(MAX-MIN) + 120.0
    elif MAX == b_new:
        H = 60.0*(r_new - g_new)/(MAX-MIN) + 240.0
        
    if MAX == 0:
        S = 0
    else:
        S = 1-(MIN/MAX)
        
    V = MAX
    
    return cornell.HSV(H, S, V)


def hsv_to_rgb(hsv):
    """
    Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    H_i = math.floor(hsv.hue/60)
    f = (hsv.hue/60) - H_i
    p = hsv.value*(1-hsv.saturation)
    q = hsv.value*(1-(f*hsv.saturation))
    t = hsv.value*(1-(1-f)*hsv.saturation)
    
    if H_i == 0:
        R = hsv.value
        G = t
        B = p
    elif H_i == 1:
        R = q
        G = hsv.value
        B = p
    elif H_i == 2:
        R = p
        G = hsv.value
        B = t
    elif H_i == 3:
        R = p
        G = q
        B = hsv.value
    elif H_i == 4:
        R = t
        G = p
        B = hsv.value
    elif H_i == 5:
        R = hsv.value
        G = p
        B = q
        
    r_finale = int(round(R*255,0))
    g_finale = int(round(G*255,0))
    b_finale = int(round(B*255,0))
    
    return cornell.RGB(r_finale, g_finale, b_finale)
