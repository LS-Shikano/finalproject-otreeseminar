

function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));

        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}


function tableCreate(start, end) {
    const body = document.getElementById("script_div"),
        tbl = document.createElement('table');

    tbl.style.width = "90%";
    tbl.style.border = '1px solid black'



    // question list
    const lst2 = ["eine ausdrucksstarke Person (ausdrucksstark und aussagekräftig in der verbalen Kommunikation)", //Q1
        "eine Person mit außergewöhnlichen rednerischen Fähigkeiten", //Q2
        "eine Person, die großen Einfluss auf andere Menschen hat", //Q3
        "eine Person, die inspiriert", //Q4
        "eine zuverlässige und glaubwürdige Person (man kann sich immer auf sie verlassen)", //Q5
        "eine ehrliche Person", //Q6
        "eine attraktive Person", //Q7
        "eine charmante Person", //Q8
        "eine Person mit positiver Energie", //Q9
        "eine Person mit einer Vision", //Q10
        "eine dominante Person (dominiert gerne und hat immer \"das Sagen\")", //Q11
        "eine Person, die Macht ausstrahlt" //Q12
     ]

    Storage.prototype.getObj = function(key) {
        return JSON.parse(this.getItem(key))
    }
    const shuffled_lst =  localStorage.getObj("Items")


    const VarNames = ["ch_Q1", "ch_Q2", "ch_Q3", "ch_Q4", "ch_Q5", "ch_Q6", "ch_Q7", "ch_Q8", "ch_Q9", "ch_Q10", "ch_Q11", "ch_Q12"]
    const ValNames = ["1", "2", "3", "4", "5"]
    const sIndex = []
    for (let i = start; i<= end; i++) {
        console.log(i)

        a = shuffled_lst[i]
        x = lst2.indexOf(a)

         sIndex.push(x)
    }
    console.log(sIndex)
    const heading = ["Die gezeigte Person ist...", "Stimme voll und ganz zu", "Ich stimme eher zu", "Weder noch",
                    "Stimme eher nicht zu", "Stimme überhaupt nicht zu"]
    //inserts the heading of the table
    const th = tbl.insertRow();
   th.style.border = '1px solid black'
    th.style.textAlign = 'center';
    th.style.backgroundColor = 'darkgrey'
     th.style.padding =  '2px', '2px', '2px', '2px';
    for (let i = 0; i < 6; i++) {
        const thd = th.insertCell();
        thd.appendChild(document.createTextNode(heading[i]));
       thd.style.border = '1px solid black'
         thd.style.padding =  '1.5px', '1.5px', '1.5px', '1.5px';

    }
    //inserts the content of the table

    var ind_count = 0
    for (let i = start; i <= end; i++) {
        const tr = tbl.insertRow();
        tr.style.border = '1px solid black'
        var counter =0 // to get the right values

        for (let j = 0; j < 6; j++) {

            if (j === 0) {
                const td = tr.insertCell();
                td.appendChild(document.createTextNode(shuffled_lst[i]));
                 td.style.border = '1px solid black'
                 td.style.padding =  '7px', '20px', '20px', '20px';
                  td.style.width = '10px'

                if (i % 2 != 0) {
                    td.style.backgroundColor = 'lightgrey'
                }
            } else {
                const td = tr.insertCell();
                td.style.border = '1px solid black';
                td.style.textAlign = 'center';
                td.style.padding =  '2px', '2px', '2px', '2px';
                td.style.width = '10px'
                if (i % 2 != 0) {
                    td.style.backgroundColor = 'lightgrey'
                }
                console.log("index")
                console.log(i)
                var c =   sIndex[ind_count]
                console.log("c")
                console.log(c)
                counter +=1


                var x = document.createElement('input');
                x.setAttribute("type", "radio");
                x.setAttribute("value", counter);
                x.setAttribute("name", VarNames[c]);
                x.setAttribute('align','center');
                x.setAttribute("class", "persist")
                td.appendChild(x);
                console.log(VarNames[c])
            }
        }
        ind_count += 1 // change var name when new row is inserted
    }

    body.appendChild(tbl);
}


