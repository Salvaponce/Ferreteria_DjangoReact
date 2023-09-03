import {useState, useEffect} from "react"
import axios from "axios"
import ListProduct from "./ListProduct"

function Product() {
    const [products , setNewProducts] = useState(null)
    const [formProduct, setFormProduct] = useState({
          name: "",
          description: "",
          image: null,
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

    /*function createProduct(event) {
        axios({
        method: "POST",
        url:"/products/",
        data:{
            name: formProduct.name,
            description: formProduct.description,
            image: formProduct.image,
            stock: formProduct.stock,
            category: formProduct.category,
            price: formProduct.price,
        }
        })
        .then((response) => {
        getProducts()
        })*/

    function createProduct(event) {
        event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada
        const formData = new FormData(); // Crea un objeto FormData para enviar el formulario
        console.log(formProduct.image);
        console.log(formProduct.image.url);
        formData.append("name", formProduct.name);
        formData.append("description", formProduct.description);
        formData.append("image", formProduct.image); // Agrega la imagen al FormData

        formData.append("stock", formProduct.stock);
        formData.append("category", formProduct.category);
        formData.append("price", formProduct.price);

        axios({
            method: "POST",
            url: "/products/",
            data: formData, // Usa el FormData en lugar de un objeto JSON
            headers: { "Content-Type": "multipart/form-data" }, // Asegura que se establezca el encabezado adecuado
        })
        .then((response) => {
            getProducts();
        })
        .catch((error) => {
            console.error("Error al crear el producto:", error);
        });

    
        setFormProduct({
          name: "",
          description: "",
          image: null,
          stock: false,
          category: "",
          price: 0,})

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
    const { name, value} = event.target;
        // Si no es un elemento de tipo 'file', actualizamos el estado como lo hacemos normalmente
        setFormProduct(prevProduct => ({
        ...prevProduct,
        [name]: value,
        }));
    }

      function handleFileChange(event) {
        const selectedFile = event.target.files[0]; // Obtén el archivo seleccionado

        setFormProduct(prevProduct => ({
        ...prevProduct,
        image: selectedFile, // Actualiza el campo 'image' en el estado con el archivo seleccionado
        }));
    }


    

    return (
      <div className=''>

            <form className="create-product" enctype="multipart/form-data">
                <input onChange={handleChange} text={formProduct.name} name="name" placeholder="Name" value={formProduct.name} />
                <textarea onChange={handleChange} name="description" placeholder="This is a description..." value={formProduct.description} />
                <input onChange={handleChange} text={formProduct.category} name="category" placeholder="category" value={formProduct.category} />
                <input onChange={handleChange} text={formProduct.price} name="price" placeholder="Price" value={formProduct.price} />

                <input
                    type="text"
                    value={formProduct.image ? formProduct.image.name : ''}
                    readOnly
                />
                <label htmlFor="fileInput">Seleccionar archivo:</label>
                <input
                    type="file"
                    id="fileInput"
                    style={{ display: 'none' }}
                    onChange={handleFileChange}
                />
                <button onClick={() => document.getElementById('fileInput').click()}>
                    Examinar
                </button>
                
                <button onClick={createProduct}>Create Product</button>
            </form>
                { products && products.map(product => <ListProduct
                key={product.id}
                id={product.id}
                name={product.name}
                description={product.description}
                image={product.image} 
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