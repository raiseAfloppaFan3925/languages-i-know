



function fib( x: number ): number {
    if ( x <= 2 ) {
        return 2;
    } else {
        return fib( x - 1 ) + fib( x - 2 );
    }
}


console.log( fib( 20 ) );

