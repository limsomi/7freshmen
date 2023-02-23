function loadFile_profile(input)
{
    var file=input.files[0];

    var newImage=document.createElement("img");
    newImage.setAttribute("class","img");

    newImage.src=URL.createObjectURL(file);

    newImage.style.width="130px";
    newImage.style.height="130px";
    newImage.style.borderRadius="50%";
    newImage.style.position="absolute"
    var button=document.getElementById("chooseFile_button");
    button.style.visibility="hidden";

    var container=document.getElementById("profile_background");
    container.appendChild(newImage);
}
function loadFile_timetable(input)
{
    var file=input.files[0];

    var newImage=document.createElement("img");
    newImage.setAttribute("class","img");

    newImage.src=URL.createObjectURL(file);

    newImage.style.width="200px";
    newImage.style.height="300px";
    newImage.style.display="flex";
    newImage.style.alignItems="center";
    newImage.style.justifyContent="center";
    var table=document.getElementById("timetable");
    table.style.height='auto';
    var container=document.getElementById("img_container");
    container.style.height='auto';
    
    container.appendChild(newImage);
}


function Save()
{
    var input=document.getElementsByClassName('inputbox')
    for (var i=0;i<input.length;i++)
    {
        var item=input.item(i);
        item.readOnly=true;
    }
    var save_button=document.getElementById('save_button');
    if(save_button.innerText=='저장')
    {
        save_button.innerText='편집';
        var input=document.getElementsByClassName('input')
        for (var i=0;i<input.length;i++)
        {
            var item=input.item(i);
            item.readOnly=true;
        }
        var table=document.getElementById('timetable_click')
        table.style.visibility="hidden";

    }
    else{
        save_button.innerText='저장';
        var input=document.getElementsByClassName('input')
        for (var i=0;i<input.length;i++)
        {
            var item=input.item(i);
            item.readOnly=false;

        }
        var table=document.getElementById('timetable_click')
        table.style.visibility="visible";
    }
}