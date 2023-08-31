function ListProduct(props){
      function handleClick(){
    props.deletion(props.id)
  }
    return (
        <div className="product">
          <h1 >  Name: {props.name} </h1>
            {props.image?.src && (
            <img src={ props.image.url } alt={ props.name } />
            )}
          <p > Description: {props.description}</p>
          <p > Price: {props.price}</p>
          <button onClick={handleClick}>Delete</button>
        </div>
    )
  }

export default ListProduct;

