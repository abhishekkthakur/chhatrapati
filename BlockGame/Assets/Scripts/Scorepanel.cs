using UnityEngine;
using UnityEngine.UI;
public class Scorepanel : MonoBehaviour
{
    public Transform player;
    public Text scorevalue;
    // Update is called once per frame
    void Update()
    {
        scorevalue.text = player.position.z.ToString("0");
    }
}
