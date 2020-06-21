class Place{
    set Locations(Locations){
        this._Locations=Locations;
    }
    set Latitude(Latitude){
        this._Latitude=Latitude;
    }
    set Longitude(Longitude){
        this._Longitude=Longitude;
    }
    get Locations(){
        return this._Locations;
    }
    get Latitude(){
        return this._Latitude;
    }
    get Longitude(){
        return this._Longitude;
    }
    constructor(){
    }
}
let pl=[];// Array to store Employee Objects
const csv=require('csvtojson')
// Invoking csv returns a promise
const converter=csv()
.fromFile('./web/locationsll.csv')
.then((json)=>{
    let e;
    json.forEach((row)=>{
        e=new Place();// New Employee Object
        Object.assign(e,row);// Assign json to the new Employee
        pl.push(e);// Add the Employee to the Array
        
    });
}).then(()=>{
    // Output the names of the Employees
    // emp.forEach((em)=>{
    //     console.log(em.Latitude);// Invoke the Name getter
    // });
    for (i = 0; i < 6; i++){
        console.log("Location: " + pl[i].Locations);
        console.log("Latidude: " + pl[i].Latitude);
        console.log("Longitude: " + pl[i].Longitude);
    }
});

