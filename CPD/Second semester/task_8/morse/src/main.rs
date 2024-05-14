fn decode_morse(encoded: &str) -> String {
    use std::collections::HashMap;
    let mut MORSE_CODE: HashMap<String, String> = HashMap::new();

        MORSE_CODE.insert(String::from(".-"), String::from("A"));
        MORSE_CODE.insert(String::from("-..."), String::from("B"));
        MORSE_CODE.insert(String::from("-.-."), String::from("C"));
        MORSE_CODE.insert(String::from("-.."), String::from("D"));
        MORSE_CODE.insert(String::from("."), String::from("E"));
        MORSE_CODE.insert(String::from("..-."), String::from("F"));
        MORSE_CODE.insert(String::from("--."), String::from("G"));
        MORSE_CODE.insert(String::from("...."), String::from("H"));
        MORSE_CODE.insert(String::from(".."), String::from("I"));
        MORSE_CODE.insert(String::from(".---"), String::from("J"));
        MORSE_CODE.insert(String::from("-.-"), String::from("K"));
        MORSE_CODE.insert(String::from(".-.."), String::from("L"));
        MORSE_CODE.insert(String::from("--"), String::from("M"));
        MORSE_CODE.insert(String::from("-."), String::from("N"));
        MORSE_CODE.insert(String::from("---"), String::from("O"));
        MORSE_CODE.insert(String::from(".--."), String::from("P"));
        MORSE_CODE.insert(String::from("--.-"), String::from("Q"));
        MORSE_CODE.insert(String::from(".-."), String::from("R"));
        MORSE_CODE.insert(String::from("..."), String::from("S"));
        MORSE_CODE.insert(String::from("-"), String::from("T"));
        MORSE_CODE.insert(String::from("..-"), String::from("U"));
        MORSE_CODE.insert(String::from("...-"), String::from("V"));
        MORSE_CODE.insert(String::from(".--"), String::from("W"));
        MORSE_CODE.insert(String::from("-..-"), String::from("X"));
        MORSE_CODE.insert(String::from("-.--"), String::from("Y"));
        MORSE_CODE.insert(String::from("--.."), String::from("Z"));
        MORSE_CODE.insert(String::from("-----"), String::from("0"));
        MORSE_CODE.insert(String::from(".----"), String::from("1"));
        MORSE_CODE.insert(String::from("..---"), String::from("2"));
        MORSE_CODE.insert(String::from("...--"), String::from("3"));
        MORSE_CODE.insert(String::from("....-"), String::from("4"));
        MORSE_CODE.insert(String::from("....."), String::from("5"));
        MORSE_CODE.insert(String::from("-...."), String::from("6"));
        MORSE_CODE.insert(String::from("--..."), String::from("7"));
        MORSE_CODE.insert(String::from("---.."), String::from("8"));
        MORSE_CODE.insert(String::from("----."), String::from("9"));
        MORSE_CODE.insert(String::from(".-.-.-"), String::from("."));
        MORSE_CODE.insert(String::from("--..--"), String::from(","));
        MORSE_CODE.insert(String::from("..--.."), String::from("?"));
        MORSE_CODE.insert(String::from(".----."), String::from("'"));
        MORSE_CODE.insert(String::from("-.-.--"), String::from("!"));
        MORSE_CODE.insert(String::from("-..-."), String::from("/"));
        MORSE_CODE.insert(String::from("-.--."), String::from("("));
        MORSE_CODE.insert(String::from("-.--.-"), String::from(")"));
        MORSE_CODE.insert(String::from(".-..."), String::from("&"));
        MORSE_CODE.insert(String::from("---..."), String::from(":"));
        MORSE_CODE.insert(String::from("-.-.-."), String::from(";"));
        MORSE_CODE.insert(String::from("-...-"), String::from("="));
        MORSE_CODE.insert(String::from(".-.-."), String::from("+"));
        MORSE_CODE.insert(String::from("-....-"), String::from("-"));
        MORSE_CODE.insert(String::from("..--.-"), String::from("_"));
        MORSE_CODE.insert(String::from(".-..-."), String::from("\""));
        MORSE_CODE.insert(String::from("...-..-"), String::from("$"));
        MORSE_CODE.insert(String::from(".--.-."), String::from("@"));
        MORSE_CODE.insert(String::from("...---..."), String::from("SOS"));

    let mut decoded_message = String::new();
    encoded.trim();
    let mut words:Vec<&str> = encoded.split("   ").collect();
    for word in words{
        let mut letters:Vec<&str> = word.split(" ").collect();
        for letter in letters{
            if letter != ""{
            let mut decoded_letter = MORSE_CODE.get(letter).unwrap();
            decoded_message += decoded_letter;
            }
        }
    decoded_message+=" "
    }
return  String::from(decoded_message.trim());
}

pub fn main() {
    let message = ".... . -.--   .--- ..- -.. .";
    let mut message = decode_morse(&message);
    println!("{:?}", message.trim())
}