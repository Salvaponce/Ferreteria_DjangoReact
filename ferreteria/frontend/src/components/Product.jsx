import {useState, useEffect} from "react"
import axios from "axios"
import ListProduct from "./ListProduct"

function Product() {
    const [products , setNewProducts] = useState(null)
    const [formProduct, setFormProduct] = useState({
          name: "",
          descripcion: "",
          imagen: "",
          stock: false,
          categoria: ""
          })

       useEffect(() => {
        getProducts()
            } ,[])

    function getProducts() {
        axios({
        method: "GET",
        url:"/products/",
        }).then((response)=>{
        const data = response.data
        setNewProducts(data)
        }).catch((error) => {
        if (error.response) {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
            }
        })}

    function createProduct(event) {
        axios({
        method: "POST",
        url:"/products/",
        data:{
            name: formProduct.name,
            descripcion: formProduct.descripcion,
            imagen: formProduct.imagen,
            stock: formProduct.stock,
            categoria: formProduct.categoria,

        }
        })
        .then((response) => {
        getProducts()
        })

    
    setFormProduct(({
          name: "",
          descrition: "",
          imagen: "",
          stock: false,
          categoria: ""}))

        event.preventDefault()
        }
    
    function DeleteNote(id) {
        axios({
        method: "DELETE",
        url:`/products/${id}/`,
        })
        .then((response) => {
        getProducts()
        });
    }  
    
    function handleChange(event) { 
        const {value, name} = event.target
        setFormProduct(prevProduct => ({
            ...prevProduct, [name]: value})
        )}

    return (
      <div className=''>

            <form className="create-product">
                <input onChange={handleChange} text={formProduct.name} name="name" placeholder="Name" value={formProduct.name} />
                <input onChange={handleChange} text={formProduct.categoria} name="categoria" placeholder="Categoria" value={formProduct.categoria} />
                <image onChange={handleChange} name="imagen" placeholder="Imagen" value={formProduct.categoria} />
                <textarea onChange={handleChange} name="descripcion" placeholder="This is a description..." value={formProduct.descripcion} />
                <button onClick={createProduct}>Create Post</button>
            </form>
                { products && products.map(product => <ListProduct
                key={product.id}
                id={product.id}
                name={product.name}
                descripcion={product.descripcion}
                imagen={product.imagen} 
                categoria = {product.categoria}
                deletion ={DeleteNote}
                />
                )}
      </div>
  );
}


export default Product;