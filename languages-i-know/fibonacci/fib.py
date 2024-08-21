import sys






def isnum( string: str ) -> bool:
    is_num: bool = True

    for char in string:
        if not char.isdigit():
            is_num = False
            break

    return is_num


if not len( sys.argv ) == 2:
    print( f"1 argument was expected but {( len( sys.argv ) - 1)} were received" )
    exit()


if not isnum( sys.argv[1] ):
    print( "That's not a number!" )
    exit()


def fib( x: int ) -> int:
    if x <= 2:
        return 1
    else:
        return fib( x - 1 ) + fib( x - 2 )



print( fib( int( sys.argv[1] ) ) )

