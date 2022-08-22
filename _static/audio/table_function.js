
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

    tbl.style.width = "100%";

    // question list
    const lst2 = ["eine ausdrucksstarke Person.", // Q1
        "eine Person mit außergewöhnlichen rednerischen Fähigkeiten.", // Q2
        "eine Person, die großen Einfluss auf andere Menschen hat.", // Q3
        "eine Person, die inspiriert.", // Q4
        "eine zuverlässige und glaubwürdige Person.", // Q5
        "eine ehrliche Person.", // Q6
        "eine attraktive Person.", // Q7
        "eine charmante Person.", // Q8
        "eine Person mit positiver Energie.", // Q9
        "eine Person mit einer Vision.", // Q10
        "eine dominante Person.", // Q11
        "eine Person, die Macht ausstrahlt." // Q12
     ]

    Storage.prototype.getObj = function(key) {
        return JSON.parse(this.getItem(key))
    }
    const shuffled_lst =  localStorage.getObj("Items")


    const VarNames = ["ch_Q1", "ch_Q2", "ch_Q3", "ch_Q4", "ch_Q5", "ch_Q6", "ch_Q7", "ch_Q8", "ch_Q9", "ch_Q10", "ch_Q11", "ch_Q12"]
    const ValNames = ["1", "2", "3", "4", "5", "6"]
    const sIndex = []
    for (let i = start; i<= end; i++) {
        // console.log(i)

        a = shuffled_lst[i]
        x = lst2.indexOf(a)

         sIndex.push(x)
    }

    const heading = ["Die gezeigte Person ist...", "Stimme überhaupt nicht zu", "Stimme eher nicht zu", "Weder noch",
                    "Stimme eher zu", "Stimme voll und ganz zu", " Weiß nicht/ Keine Angabe"]

    //inserts the heading of the table
    const th = tbl.insertRow();
   //th.style.border = '1px solid black'

    //th.style.backgroundColor = 'darkgrey'
     //th.style.padding =  '5px', '5px', '5px', '5px';
    for (let i = 0; i < 7; i++) {
        const thd = th.insertCell();
        ele = document.createElement("B")
        text = document.createTextNode(heading[i])
        ele.appendChild(text)
        thd.appendChild(ele);
        thd.style.paddingBottom = '10px'
        thd.style.paddingLeft = '10px'
        if (i == 0){
        thd.style.textAlign = 'left'
    }
    else {
        thd.style.textAlign = 'center';
    }


    }
    //inserts the content of the table

    var ind_count = 0
    for (let i = start; i <= end; i++) {
        const tr = tbl.insertRow();
        //tr.style.border = '1px solid black'
        var counter =0 // to get the right values

        for (let j = 0; j < 7; j++) {

            // first column
            if (j == 0 ) {
                const td = tr.insertCell();
                ele2 = document.createElement("B")
                ques = document.createTextNode(shuffled_lst[i])
                ele2.appendChild(ques)
                td.appendChild(ele2);
                // black line at top
                if (i == 0 || i == 6) {
                    td.style.borderTop = '1px solid black'
                }
                // line at bottom
                else if (i == 5 || i == 11){
                    td.style.borderBottom = 'solid 1px rgb(220,220,220)'
                    td.style.borderTop = 'solid 1px rgb(220,220,220)'
                }
                // noraml row lines
                else{
                    td.style.borderTop = 'solid 1px rgb(220,220,220)'
                }
                td.style.padding =  '15px';
                td.style.width = '5px'


            // columns 2-6
            } else {
                const td = tr.insertCell();
                // black line at top
                if (i == 0 || i == 6) {
                    td.style.borderTop = '1px solid black'
                }
                // line at bottom
                else if(i == 5 || i == 11){
                    td.style.borderBottom = 'solid 1px rgb(220,220,220)'
                    td.style.borderTop = 'solid 1px rgb(220,220,220)'
                }
                // normal row lines
                else{
                    td.style.borderTop = 'solid 1px rgb(220,220,220)'
                }
                // line keine Angabe
                if (j == 6) {
                    td.style.borderLeft = 'solid 1px rgb(220,220,220)'
                }
               td.style.textAlign = 'center';
               td.style.padding =  '10px';
               td.style.width = '5px'

                var c =   sIndex[ind_count]
                counter +=1

                // create the radio buttons
                var x = document.createElement('input');
                x.setAttribute("type", "radio");
                x.setAttribute("value", counter);
                x.setAttribute("name", VarNames[c]);
                x.setAttribute('align','center');
                td.appendChild(x);
                // console.log(VarNames[c])
            }
        }
        ind_count += 1 // change var name when new row is inserted
    }

    body.appendChild(tbl);
}


