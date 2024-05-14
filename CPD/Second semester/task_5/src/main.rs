
pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    nums.sort();
    nums.dedup();
    return nums.len() as i32;
}

fn main(){
    let mut nums = [1,1,2];
    remove_duplicates(nums);

}