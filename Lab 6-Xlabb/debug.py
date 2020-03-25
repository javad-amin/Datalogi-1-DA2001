def bubblesort(lst):
    """
    Sortera listan med bubbelsortering. Det finns en bugg!
    Listan `lst` är en lista med tal.
    Funktionen ändrar på den ursprungliga listan.
    """
    N = len(lst)
    for repetition in range(N-1):
        for i in range(N-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

if __name__ == "__main__":
    my_list = [2,1,6,2,1,10,5,3,8,1]
    print(bubblesort(my_list))
	
import debug
import imp