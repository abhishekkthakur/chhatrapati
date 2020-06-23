using UnityEngine;

public class PlayerMovement : MonoBehaviour
{

    public Rigidbody rb;

    public float forwardforce = 250f;
    public float sidewaysforce = 250f;
    public float verticalforce = 1f;
    // Update is called once per frame
    void FixedUpdate()
    {
        rb.AddForce(0, 0, forwardforce * Time.deltaTime);

        if ( Input.GetKey("d") )
        {
            rb.AddForce(sidewaysforce * Time.deltaTime, 0, 0, ForceMode.VelocityChange);  
		}

        if ( Input.GetKey("a") )
        {
            rb.AddForce(-sidewaysforce * Time.deltaTime, 0, 0, ForceMode.VelocityChange);  
		}

        if ( Input.GetKey("w") )
        {
            rb.AddForce(0, 0, forwardforce * Time.deltaTime);  
		}

        if ( Input.GetKey("s") )
        {
            rb.AddForce(0, 0, - 2 * forwardforce * Time.deltaTime);  
		}

        /*
        if ( Input.GetKey("space") )
        {
            rb.AddForce(0, verticalforce, 0, ForceMode.VelocityChange);  
		}
        */

        if (rb.position.y < -0.5f)
        {
            FindObjectOfType<GameManager>().EndGame();  
		}

    }
}
