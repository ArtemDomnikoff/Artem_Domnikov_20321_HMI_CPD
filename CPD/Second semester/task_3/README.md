## 1_1
max area
## Листинг 1_1
```rs
fn max_area(height: Vec<i32>) -> i32 {
    let (mut left, mut right) = (0, height.len() - 1);
    let mut max_area = 0;
    while left < right {
        let width: i32 = (right - left) as i32;
        let min_height = std::cmp::min(height[left], height[right]);
        let current_area = width * min_height;
        max_area = std::cmp::max(max_area, current_area);

        // Move the pointer of the shorter line inward
        if height[left] < height[right] {
            left += 1;
        } else {
            right -= 1;
        }
    }

    // Return the maximum area found
    max_area
}
fn main(){
    let s:&str = "Abra Kadabra ";
    let r = length_of_last_word(s);
    println!("{}", r)
}
```

### Результат выполнения программы
![alt text](image.png)
### Пояснение
Дан целочисленный массив высоты длинной n. Нарисовано n вертикальных линий, конечными точками которых являются (i, 0) и (i, height[i]).
Задаются две переменные, указывающие на максимальную высоту левого и правого столбцов.После задаётся переменная максимальной площади.
в цикле пока высота левого столбца меньше высоты правого, вычисляется ширина и высота между столбцами, после вычисляется площадь. Если вычисленная площадь больше нынешней максиммальной, то вычисленная площадь становится максимальной.Указатель на кратчайший столб передвигается в зависимости от того, где находится кратчайший столб.

Возвращает максимальное количество воды, которое может хранить контейнер.
