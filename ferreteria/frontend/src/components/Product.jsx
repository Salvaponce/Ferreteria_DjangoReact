import {useState, useEffect} from "react"
import axios from "axios"
import ListProduct from "./ListProduct"

function Product() {
    const [products , setNewProducts] = useState(null)
    const [formProduct, setFormProduct] = useState({
          name: "",
          description: "",
          imagen: "",
          stock: false,
          category: "",
          price: 0,
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
            description: formProduct.description,
            imagen: formProduct.imagen,
            stock: formProduct.stock,
            category: formProduct.category,
            price: formProduct.price,
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
          category: "",
          price: 0}))

        event.preventDefault()
        }
    
    function DeleteProduct(id) {
        axios({
        method: "DELETE",
        url:`/products/${id}/`,
        })
        .then((response) => {
        getProducts()
        });
    } 
    
    function AddCart(id){
        axios({
            method: "GET",
            url: `/products/${id}`,
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
                <textarea onChange={handleChange} name="description" placeholder="This is a description..." value={formProduct.description} />
                <input onChange={handleChange} text={formProduct.category} name="category" placeholder="category" value={formProduct.category} />
                <input onChange={handleChange} text={formProduct.price} name="price" placeholder="Price" value={formProduct.price} />
                <button onClick={createProduct}>Create Product</button>
            </form>
                { products && products.map(product => <ListProduct
                key={product.id}
                id={product.id}
                name={product.name}
                description={product.description}
                imagen={product.imagen} 
                category = {product.category}
                price = {product.price}
                deletion ={DeleteProduct}
                cart = {AddCart}
                />
                )}
      </div>
  );
}


export default Product;