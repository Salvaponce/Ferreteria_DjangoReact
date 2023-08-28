function ListProduct(props){
      function handleClick(){
    props.deletion(props.id)
  }
    return (
        <div className="product">
          <h1 >  Name: {props.name} </h1>
          <p > Description: {props.description}</p>
          <button onClick={handleClick}>Delete</button>
        </div>
    )
  }

export default ListProduct;

