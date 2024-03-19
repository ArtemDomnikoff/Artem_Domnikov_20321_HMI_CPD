fn length_of_last_word(s: &str) -> i32 {
    let mut count = 0;
    
    for chr in s.trim_end().chars().rev() {
        if chr == ' ' {
            break
        } else {
            count += 1;
        }
    }
    
    count
}

fn main(){
    let s:&str = "Abra Kadabra ";
    let r = length_of_last_word(s);
    println!("{}", r)
}