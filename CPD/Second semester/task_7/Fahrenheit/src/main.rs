use std::io;

fn main() {
    println!("Введите температуру в Фаренгейтах:");
    let mut fahrenheit = String::new();
    io::stdin().read_line(&mut fahrenheit).expect("Не удалось прочитать строку");
    let fahrenheit: f32 = fahrenheit.trim().parse().expect("Пожалуйста, введите число");
    let celsius = (fahrenheit - 32.0) * 5.0 / 9.0;
    println!("{:.2} Фаренгейт = {:.2} Цельсий", fahrenheit, celsius);
}
