## 1_1
longest common prefix
## Листинг 1_1
```rs
pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
    let len = matrix.len() - 1;
    let half = (matrix.len() + 1) / 2;

    for row in 0..half {
        for column in row..(len - row) {
            let (a, b, c, d) =
                (
                matrix[row][column],
                matrix[column][len - row],
                matrix[len - row][len - column],
                matrix[len - column][row]
                );

            matrix[row][column] = d;
            matrix[column][len - row] = a;
            matrix[len - row][len - column] = b;
            matrix[len - column][row] = c;
        }
    }
}

fn main(){
    let mut matrix = vec![vec![1,2,3],vec![4,5,6],vec![7,8,9]];
    println!("{:?}", matrix);
    rotate(&mut matrix);
    println!("{:?}", matrix);
}
```

### Результат выполнения программы
![alt text](image.png)