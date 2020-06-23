using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    bool gameHasEnded = false;  
    public float restartTime = 1f;

    public GameObject completeLevelUI;

    public void EndGame ()
    {
        if (gameHasEnded == false)
        {
            gameHasEnded = true;
            Debug.Log("GAME OVER");
            Invoke("Restart", restartTime);
		}  
	}

    void Restart ()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);            
	}

    public void CompleteLevel ()
    {
        //Debug.Log("Level Won!");
        completeLevelUI.SetActive(true);
	}

}
