## 1_1
Decode morse code 2
## Листинг 1_1
```rs
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

fn decode_bits(encoded: &str) -> String{
    let mut decoded_message = String::new();
    let charTypeSeparator = "0".repeat(1);
    let charSeparator = "0".repeat(3);
    let wordSeparator = "0".repeat(7);
    let words: Vec<_> = encoded.split(&wordSeparator).collect();
    for word in words{
        if word != ""{
        let letters:Vec<_> = word.split(&charSeparator).collect();
        for letter in letters{
            if letter != ""{
            let  mut decoded_letter = String::new();
            let  elements:Vec<_> = letter.split(&charTypeSeparator).collect();  
            for element in elements{
                if element != ""{
                    if element == "11"{
                        decoded_letter += ".";
                    
                    }
                    else if element == "111111"{
                        decoded_letter += "-"
                    }                      
                }
            }
            decoded_message+=&decoded_letter;
            decoded_message+=" "; 
            }
        }
        }
        decoded_message = String::from(decoded_message.trim());
        decoded_message+="   ";
    }
    
    return String::from(decoded_message.trim())
}

pub fn main() {
    let message = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011";
    let message = decode_bits(&message);
    let message = decode_morse(&message);
    println!("{:?}", message)   
}
```

### Результат выполнения программы
![alt text](image.png)
