function abc() {
  const a = document.createTextNode('ssafy')
  const b = document.createElement('div')
  b.append(a)
  const bd = document.querySelector('body')
  b.setAttribute('class', 'asdf')
  bd.append(b)
}


const bt = document.querySelector('.asdf')
bt.addEventListener('click', abc)