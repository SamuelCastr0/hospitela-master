function toggleActive(){
    const symptomsListItems = document.querySelectorAll('[data-symptoms="item"]')
    console.log(symptomsListItems)
    symptomsListItems.forEach( symptom => {
        symptom.addEventListener( 'click',event => {
            event.preventDefault();
            event.stopPropagation();
            symptom.classList.toggle('active');
        })
    })
}

toggleActive()


// function markUnmarkCheckBox(checkBox) {
//     checkBox.checked = checkBox.checked ? false : true;
// }
//
// // function modalsData() {
// //     divs = document.querySelectorAll('[data-symptoms="item"]')
// //
// //     divs.forEach( div => {
// //         const pk = div.querySelector('input').value;
// //         console.log(pk);
// //     })
// // }
//
// function showAndHideConfig(item){
//     const menu = item.querySelector('[data-config]')
//     const points = item.querySelector('[data-points]')
//
//     points.addEventListener('click', event => {
//         event.stopPropagation()
//         menu.classList.add('active')
//     })
//     menu.addEventListener('mouseleave', event => {
//         event.stopPropagation()
//         menu.classList.remove('active')
//     })
// }
//
// function addVisualEventsToSymptomsList(){
//     let symptomsListItems = document.querySelectorAll('[data-symptoms="item"]')
//
//     symptomsListItems.forEach(item => {
//         let flagToMark = false
//             const child = item.querySelector('[data-symptoms="label"]')
//             item.addEventListener('click', event => {
//             event.preventDefault()
//             if(!flagToMark) {
//                 child.classList.add('active')
//                 flagToMark = true
//                 markUnmarkCheckBox(child.querySelector('input'))
//             } else if(flagToMark) {
//                 flagToMark = false
//                 child.classList.remove('active')
//                 markUnmarkCheckBox(child.querySelector('input'))
//             }
//         })
//             const points = item.querySelector('[data-points]')
//
//         item.addEventListener('mouseleave', event => {
//             event.preventDefault()
//             points.classList.remove('active')
//             if(!flagToMark) child.classList.remove('active')
//         })
//
//         item.addEventListener('mouseover', event => {
//             event.preventDefault()
//             points.classList.add('active')
//              if(!flagToMark) {
//                  child.classList.add('active')
//              }
//         })
//         showAndHideConfig(item)
//     })
// }
//
// // modalsData()
// addVisualEventsToSymptomsList()
