function palindrome(str) {
  for (let i=0; i < Math.floor(str.length / 2); i++) {
    let left = str[i]
    let right = str[str.length - 1 - i]
    if (left != right) {
      console.log('false')
      return
    }
  }
  console.log('true')
  return
}

  // 출력
  // palindrome('level') => true
  // palindrome('hi') => false