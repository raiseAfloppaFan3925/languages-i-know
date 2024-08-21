


use std::env;



fn fib( x: u128 ) -> u128 {
    if x <= 2 {
        1
    } else {
        fib( x - 1 ) + fib( x - 2 )
    }
}



fn main() {

    let args: Vec<String> = env::args().collect();

    if args.len() != 2 as usize {
        if args.len() > 2 {
            println!( "Too much arguments!" );
        } else {
            println!( "Too little arguments!" );
        }
    }

    println!( "{}", fib( args[1].parse().expect( "That's not an integer!" ) ) );
    
}


