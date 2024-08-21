extends Node




func _ready() -> void:
    print( "The 20th term in the fibonacci sequence is ", fib( 20 ) )



func fib( x: int ) -> int:
    if x <= 2:
        return 1
    else:
        return fib( x - 1 ) + fib( x - 2 )

